import FWCore.ParameterSet.Config as cms

def SimTrackSimVertexDumper(**kwargs):
  mod = cms.EDAnalyzer('SimTrackSimVertexDumper',
    moduleLabelHepMC = cms.InputTag('generatorSmeared'),
    moduleLabelTk = cms.InputTag('g4SimHits'),
    moduleLabelVtx = cms.InputTag('g4SimHits'),
    dumpHepMC = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
