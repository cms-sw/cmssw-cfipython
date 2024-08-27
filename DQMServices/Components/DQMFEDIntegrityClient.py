import FWCore.ParameterSet.Config as cms

def DQMFEDIntegrityClient(**kwargs):
  mod = cms.EDAnalyzer('DQMFEDIntegrityClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
