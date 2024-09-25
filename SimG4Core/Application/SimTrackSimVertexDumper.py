import FWCore.ParameterSet.Config as cms

def SimTrackSimVertexDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('SimTrackSimVertexDumper',
    moduleLabelHepMC = cms.InputTag('generatorSmeared'),
    moduleLabelTk = cms.InputTag('g4SimHits'),
    moduleLabelVtx = cms.InputTag('g4SimHits'),
    dumpHepMC = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
