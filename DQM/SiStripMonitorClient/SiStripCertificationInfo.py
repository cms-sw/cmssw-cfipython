import FWCore.ParameterSet.Config as cms

def SiStripCertificationInfo(**kwargs):
  mod = cms.EDAnalyzer('SiStripCertificationInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
