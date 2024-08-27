import FWCore.ParameterSet.Config as cms

def SiStripBadComponentsDQMServiceReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadComponentsDQMServiceReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
