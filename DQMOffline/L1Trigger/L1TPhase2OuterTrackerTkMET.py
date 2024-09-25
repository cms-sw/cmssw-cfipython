import FWCore.ParameterSet.Config as cms

def L1TPhase2OuterTrackerTkMET(*args, **kwargs):
  mod = cms.EDProducer('L1TPhase2OuterTrackerTkMET',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
