import FWCore.ParameterSet.Config as cms

def TestReadRun2Scouting(**kwargs):
  mod = cms.EDAnalyzer('TestReadRun2Scouting',
    expectedCaloJetsValues = cms.required.vdouble,
    caloJetsTag = cms.required.InputTag,
    expectedElectronFloatingPointValues = cms.required.vdouble,
    expectedElectronIntegralValues = cms.required.vint32,
    electronsTag = cms.required.InputTag,
    muonClassVersion = cms.required.int32,
    expectedMuonFloatingPointValues = cms.required.vdouble,
    expectedMuonIntegralValues = cms.required.vint32,
    muonsTag = cms.required.InputTag,
    expectedParticleFloatingPointValues = cms.required.vdouble,
    expectedParticleIntegralValues = cms.required.vint32,
    particlesTag = cms.required.InputTag,
    expectedPFJetFloatingPointValues = cms.required.vdouble,
    expectedPFJetIntegralValues = cms.required.vint32,
    pfJetsTag = cms.required.InputTag,
    expectedPhotonFloatingPointValues = cms.required.vdouble,
    photonsTag = cms.required.InputTag,
    trackClassVersion = cms.required.int32,
    expectedTrackFloatingPointValues = cms.required.vdouble,
    expectedTrackIntegralValues = cms.required.vint32,
    tracksTag = cms.required.InputTag,
    vertexClassVersion = cms.required.int32,
    expectedVertexFloatingPointValues = cms.required.vdouble,
    expectedVertexIntegralValues = cms.required.vint32,
    vertexesTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
