import FWCore.ParameterSet.Config as cms

def PATTauCandidatesRekeyer(*args, **kwargs):
  mod = cms.EDProducer('PATTauCandidatesRekeyer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
