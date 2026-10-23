import FWCore.ParameterSet.Config as cms

def PATElectronCandidatesRekeyer(*args, **kwargs):
  mod = cms.EDProducer('PATElectronCandidatesRekeyer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
