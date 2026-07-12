import FWCore.ParameterSet.Config as cms

def TruthGraphDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('TruthGraphDumper',
    src = cms.InputTag('truthGraphProducer'),
    dotFile = cms.string('truthgraph.dot'),
    maxNodes = cms.uint32(5000),
    maxEdgesPerNode = cms.uint32(200),
    simTracks = cms.InputTag('g4SimHits'),
    simVertices = cms.InputTag('g4SimHits'),
    genEventHepMC = cms.InputTag('generatorSmeared'),
    genEventHepMC3 = cms.InputTag('generatorSmeared'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
