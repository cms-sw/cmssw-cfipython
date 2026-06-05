import FWCore.ParameterSet.Config as cms

def PATJetCandidatesRekeyer(*args, **kwargs):
  mod = cms.EDProducer('PATJetCandidatesRekeyer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
