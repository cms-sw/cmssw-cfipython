import FWCore.ParameterSet.Config as cms

def L1TPhase2OuterTrackerTkMET(**kwargs):
  mod = cms.EDProducer('L1TPhase2OuterTrackerTkMET',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
