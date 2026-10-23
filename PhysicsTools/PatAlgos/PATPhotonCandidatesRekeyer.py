import FWCore.ParameterSet.Config as cms

def PATPhotonCandidatesRekeyer(*args, **kwargs):
  mod = cms.EDProducer('PATPhotonCandidatesRekeyer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
