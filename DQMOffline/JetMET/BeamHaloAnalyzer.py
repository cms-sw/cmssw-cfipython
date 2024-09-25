import FWCore.ParameterSet.Config as cms

def BeamHaloAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('BeamHaloAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
