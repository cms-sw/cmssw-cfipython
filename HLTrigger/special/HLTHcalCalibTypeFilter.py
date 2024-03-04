import FWCore.ParameterSet.Config as cms

def HLTHcalCalibTypeFilter(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
