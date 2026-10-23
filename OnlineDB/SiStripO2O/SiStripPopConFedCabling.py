import FWCore.ParameterSet.Config as cms

def SiStripPopConFedCabling(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPopConFedCabling',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
