import FWCore.ParameterSet.Config as cms

def BeamDivergenceVtxGenerator(**kwargs):
  mod = cms.EDProducer('BeamDivergenceVtxGenerator',
    src = cms.InputTag('generator', 'unsmeared'),
    srcGenParticle = cms.VInputTag(),
    simulateBeamDivergence = cms.bool(True),
    simulateVertex = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
