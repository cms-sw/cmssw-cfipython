import FWCore.ParameterSet.Config as cms

def TrackDeepNNTagInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackDeepNNTagInfoProducer',
    svTagInfos = cms.InputTag(''),
    computer = cms.PSet(
      trackPseudoSelection = cms.PSet(
        max_pT_dRcut = cms.double(0.1),
        b_dR = cms.double(0.6263),
        min_pT = cms.double(120),
        b_pT = cms.double(0.3684),
        ptMin = cms.double(0),
        max_pT_trackPTcut = cms.double(3),
        max_pT = cms.double(500),
        useVariableJTA = cms.bool(False),
        maxDecayLen = cms.double(5),
        qualityClass = cms.string('any'),
        normChi2Max = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dValMin = cms.double(-99999.9),
        a_dR = cms.double(-0.001053),
        maxDistToAxis = cms.double(0.07),
        totalHitsMin = cms.uint32(3),
        a_pT = cms.double(0.005263),
        sip2dSigMax = cms.double(99999.9),
        sip2dValMax = cms.double(99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dValMax = cms.double(99999.9),
        min_pT_dRcut = cms.double(0.5),
        jetDeltaRMax = cms.double(0.3),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip2dSigMin = cms.double(2)
      ),
      trackSelection = cms.PSet(
        max_pT_dRcut = cms.double(0.1),
        b_dR = cms.double(0.6263),
        min_pT = cms.double(120),
        b_pT = cms.double(0.3684),
        ptMin = cms.double(0),
        max_pT_trackPTcut = cms.double(3),
        max_pT = cms.double(500),
        useVariableJTA = cms.bool(False),
        maxDecayLen = cms.double(5),
        qualityClass = cms.string('any'),
        normChi2Max = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dValMin = cms.double(-99999.9),
        a_dR = cms.double(-0.001053),
        maxDistToAxis = cms.double(0.07),
        totalHitsMin = cms.uint32(3),
        a_pT = cms.double(0.005263),
        sip2dSigMax = cms.double(99999.9),
        sip2dValMax = cms.double(99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dValMax = cms.double(99999.9),
        min_pT_dRcut = cms.double(0.5),
        jetDeltaRMax = cms.double(0.3),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip2dSigMin = cms.double(-99999.9)
      ),
      trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
      ),
      pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
      ),
      trackFlip = cms.bool(False),
      useTrackWeights = cms.bool(True),
      SoftLeptonFlip = cms.bool(False),
      pseudoMultiplicityMin = cms.uint32(2),
      correctVertexMass = cms.bool(True),
      minimumTrackWeight = cms.double(0.5),
      charmCut = cms.double(1.5),
      trackSort = cms.string('sip2dSig'),
      trackMultiplicityMin = cms.uint32(2),
      vertexFlip = cms.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
