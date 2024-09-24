import FWCore.ParameterSet.Config as cms

def HLTPFTauIPFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPFTauIPFilter',
    saveTags = cms.bool(True),
    Taus = cms.InputTag('hltTauCollection'),
    TausIP = cms.InputTag('hltTauIPCollection'),
    MinN = cms.int32(1),
    TriggerType = cms.int32(84),
    Cut = cms.string('dxy > -999.'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
