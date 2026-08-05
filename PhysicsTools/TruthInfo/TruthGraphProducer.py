import FWCore.ParameterSet.Config as cms

def TruthGraphProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthGraphProducer',
    genEventHepMC3 = cms.InputTag('generatorSmeared'),
    genEventHepMC = cms.InputTag('generatorSmeared'),
    simTracks = cms.InputTag('g4SimHits'),
    simVertices = cms.InputTag('g4SimHits'),
    addGenToSimEdges = cms.bool(True),
    collapseGenShower = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
