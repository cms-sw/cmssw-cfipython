import FWCore.ParameterSet.Config as cms

def BeamHaloAnalyzer(**kwargs):
  mod = cms.EDProducer('BeamHaloAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
