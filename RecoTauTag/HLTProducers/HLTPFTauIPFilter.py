import FWCore.ParameterSet.Config as cms

def HLTPFTauIPFilter(**kwargs):
  mod = cms.EDFilter('HLTPFTauIPFilter',
    saveTags = cms.bool(True),
    Taus = cms.InputTag('hltTauCollection'),
    TausIP = cms.InputTag('hltTauIPCollection'),
    MinN = cms.int32(1),
    TriggerType = cms.int32(84),
    Cut = cms.string('dxy > -999.'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
