import FWCore.ParameterSet.Config as cms

def BeamDivergenceVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('BeamDivergenceVtxGenerator',
    src = cms.InputTag('generator', 'unsmeared'),
    srcGenParticle = cms.VInputTag(),
    simulateBeamDivergence = cms.bool(True),
    simulateVertex = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
