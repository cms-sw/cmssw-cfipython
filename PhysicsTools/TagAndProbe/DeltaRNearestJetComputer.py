import FWCore.ParameterSet.Config as cms

def DeltaRNearestJetComputer(*args, **kwargs):
  mod = cms.EDProducer('DeltaRNearestJetComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
