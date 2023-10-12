/** @odoo-module alias=hr_timesheet.task_with_hours **/

import field_registry from 'web.field_registry';
var UpgradeBoolean = field_registry.get('upgrade_boolean');
var UpgradeRadio = field_registry.get('upgrade_radio');

if (!UpgradeBoolean){
    return;
}
var include = {
    _render: function () {
        this.$el.parent().parent().remove();
    }
};
UpgradeRadio.include(include);
UpgradeBoolean.include(include);

