import FWCore.ParameterSet.Config as cms

def SiStripCertificationInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCertificationInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
