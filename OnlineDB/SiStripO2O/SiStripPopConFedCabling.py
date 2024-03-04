import FWCore.ParameterSet.Config as cms

def SiStripPopConFedCabling(**kwargs):
  mod = cms.EDAnalyzer('SiStripPopConFedCabling',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
