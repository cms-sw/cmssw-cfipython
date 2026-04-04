import FWCore.ParameterSet.Config as cms

def HcalLutMetadataPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalLutMetadataPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
