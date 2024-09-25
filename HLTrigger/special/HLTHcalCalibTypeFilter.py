import FWCore.ParameterSet.Config as cms

def HLTHcalCalibTypeFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTHcalCalibTypeFilter',
    InputTag = cms.InputTag('source'),
    CalibTypes = cms.vint32(
      1,
      2,
      3,
      4,
      5
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
