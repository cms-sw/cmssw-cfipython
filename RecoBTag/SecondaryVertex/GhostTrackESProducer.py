import FWCore.ParameterSet.Config as cms

def GhostTrackESProducer(*args, **kwargs):
  mod = cms.ESProducer('GhostTrackESProducer',
    charmCut = cms.double(1.5),
    trackSort = cms.string('sip2dSig'),
    trackSelection = cms.PSet(
      pixelHitsMin = cms.uint32(0),
      totalHitsMin = cms.uint32(0),
      ptMin = cms.double(0),
      normChi2Max = cms.double(99999.9),
      jetDeltaRMax = cms.double(0.3),
      maxDistToAxis = cms.double(0.07),
      maxDecayLen = cms.double(5),
      sip2dValMin = cms.double(-99999.9),
      sip2dValMax = cms.double(99999.9),
      sip2dSigMin = cms.double(-99999.9),
      sip2dSigMax = cms.double(99999.9),
      sip3dValMin = cms.double(-99999.9),
      sip3dValMax = cms.double(99999.9),
      sip3dSigMin = cms.double(-99999.9),
      sip3dSigMax = cms.double(99999.9),
      useVariableJTA = cms.bool(False),
      qualityClass = cms.string(''),
      a_dR = cms.double(-0.001053),
      b_dR = cms.double(0.6263),
      a_pT = cms.double(0.005263),
      b_pT = cms.double(0.3684),
      min_pT = cms.double(120),
      max_pT = cms.double(500),
      min_pT_dRcut = cms.double(0.5),
      max_pT_dRcut = cms.double(0.1),
      max_pT_trackPTcut = cms.double(3)
    ),
    minimumTrackWeight = cms.double(0),
    trackPairV0Filter = cms.PSet(
      k0sMassWindow = cms.double(0)
    ),
    useCategories = cms.bool(False),
    categoryVariableName = cms.string(''),
    calibrationRecords = cms.vstring(),
    calibrationRecord = cms.string(''),
    recordLabel = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
