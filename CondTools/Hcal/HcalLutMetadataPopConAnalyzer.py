import FWCore.ParameterSet.Config as cms

def HcalLutMetadataPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalLutMetadataPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
