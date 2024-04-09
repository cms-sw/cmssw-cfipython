import FWCore.ParameterSet.Config as cms

def TestWriteRun3Scouting(**kwargs):
  mod = cms.EDProducer('TestWriteRun3Scouting',
    caloJetsValues = cms.required.vdouble,
    electronsFloatingPointValues = cms.required.vdouble,
    electronsIntegralValues = cms.required.vint32,
    muonsFloatingPointValues = cms.required.vdouble,
    muonsIntegralValues = cms.required.vint32,
    particlesFloatingPointValues = cms.required.vdouble,
    particlesIntegralValues = cms.required.vint32,
    pfJetsFloatingPointValues = cms.required.vdouble,
    pfJetsIntegralValues = cms.required.vint32,
    photonsFloatingPointValues = cms.required.vdouble,
    photonsIntegralValues = cms.required.vint32,
    tracksFloatingPointValues = cms.required.vdouble,
    tracksIntegralValues = cms.required.vint32,
    vertexesFloatingPointValues = cms.required.vdouble,
    vertexesIntegralValues = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod