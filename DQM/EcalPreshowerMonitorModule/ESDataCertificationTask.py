import FWCore.ParameterSet.Config as cms

def ESDataCertificationTask(*args, **kwargs):
  mod = cms.EDAnalyzer('ESDataCertificationTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
