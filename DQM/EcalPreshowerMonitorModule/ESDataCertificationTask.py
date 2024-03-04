import FWCore.ParameterSet.Config as cms

def ESDataCertificationTask(**kwargs):
  mod = cms.EDAnalyzer('ESDataCertificationTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
