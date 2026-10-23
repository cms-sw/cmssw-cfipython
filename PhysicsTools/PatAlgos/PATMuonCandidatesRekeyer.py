import FWCore.ParameterSet.Config as cms

def PATMuonCandidatesRekeyer(*args, **kwargs):
  mod = cms.EDProducer('PATMuonCandidatesRekeyer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
