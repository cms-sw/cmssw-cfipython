import FWCore.ParameterSet.Config as cms

def ElectronNHitSeedProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronNHitSeedProducer',
    initialSeeds = cms.InputTag('hltElePixelSeedsCombined'),
    vertices = cms.InputTag(''),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    measTkEvt = cms.InputTag('hltSiStripClusters'),
    superClusters = cms.VInputTag('hltEgammaSuperClustersToPixelMatch'),
    matcherConfig = cms.PSet(
      useRecoVertex = cms.bool(False),
      enableHitSkipping = cms.bool(False),
      requireExactMatchCount = cms.bool(True),
      useParamMagFieldIfDefined = cms.bool(True),
      paramMagField = cms.ESInputTag('', 'ParabolicMf'),
      navSchool = cms.ESInputTag('', 'SimpleNavigationSchool'),
      detLayerGeom = cms.ESInputTag('', 'hltESPGlobalDetLayerGeometry'),
      minNrHitsValidLayerBins = cms.vint32(4),
      minNrHits = cms.vuint32(
        2,
        3
      ),
      matchingCuts = cms.VPSet(
        cms.PSet(
          dPhiMax = cms.double(0.04),
          dRZMax = cms.double(0.09),
          dRZMaxLowEt = cms.vdouble(
            0.09,
            0.09,
            0.09
          ),
          dRZMaxLowEtEtaBins = cms.vdouble(
            1,
            1.5
          ),
          dRZMaxLowEtThres = cms.double(0.09),
          version = cms.int32(1)
        ),
        cms.PSet(
          dPhiMax = cms.double(0.04),
          dRZMax = cms.double(0.09),
          dRZMaxLowEt = cms.vdouble(
            0.09,
            0.09,
            0.09
          ),
          dRZMaxLowEtEtaBins = cms.vdouble(
            1,
            1.5
          ),
          dRZMaxLowEtThres = cms.double(0.09),
          version = cms.int32(1)
        ),
        cms.PSet(
          dPhiMax = cms.double(0.04),
          dRZMax = cms.double(0.09),
          dRZMaxLowEt = cms.vdouble(
            0.09,
            0.09,
            0.09
          ),
          dRZMaxLowEtEtaBins = cms.vdouble(
            1,
            1.5
          ),
          dRZMaxLowEtThres = cms.double(0.09),
          version = cms.int32(1)
        )
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
