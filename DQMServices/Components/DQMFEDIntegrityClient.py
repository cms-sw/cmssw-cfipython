import FWCore.ParameterSet.Config as cms

def DQMFEDIntegrityClient(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMFEDIntegrityClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
