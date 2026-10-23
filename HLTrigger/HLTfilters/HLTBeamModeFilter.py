import FWCore.ParameterSet.Config as cms

def HLTBeamModeFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTBeamModeFilter',
    saveTags = cms.bool(True),
    L1GtEvmReadoutRecordTag = cms.InputTag('gtEvmDigis'),
    AllowedBeamMode = cms.vuint32(11),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
