import FWCore.ParameterSet.Config as cms

def PPSAssociationCutsESSource(*args, **kwargs):
  mod = cms.ESSource('PPSAssociationCutsESSource',
    ppsAssociationCutsLabel = cms.string(''),
    configuration = cms.VPSet(
      template = cms.PSetTemplate(
        validityRange = cms.EventRange('0:18446744073709551615-0:18446744073709551615'),
        association_cuts_45 = cms.PSet(
          x_cut_mean = cms.string(''),
          x_cut_threshold = cms.string(''),
          y_cut_mean = cms.string(''),
          y_cut_threshold = cms.string(''),
          xi_cut_mean = cms.string(''),
          xi_cut_threshold = cms.string(''),
          th_y_cut_mean = cms.string(''),
          th_y_cut_threshold = cms.string(''),
          ti_tr_min = cms.double(-1),
          ti_tr_max = cms.double(1)
        ),
        association_cuts_56 = cms.PSet(
          x_cut_mean = cms.string(''),
          x_cut_threshold = cms.string(''),
          y_cut_mean = cms.string(''),
          y_cut_threshold = cms.string(''),
          xi_cut_mean = cms.string(''),
          xi_cut_threshold = cms.string(''),
          th_y_cut_mean = cms.string(''),
          th_y_cut_threshold = cms.string(''),
          ti_tr_min = cms.double(-1),
          ti_tr_max = cms.double(1)
        )
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
