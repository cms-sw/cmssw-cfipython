import FWCore.ParameterSet.Config as cms

electronNHitSeedProducer = cms.EDProducer('ElectronNHitSeedProducer',
  initialSeeds = cms.InputTag('hltElePixelSeedsCombined'),
  vertices = cms.InputTag(''),
  beamSpot = cms.InputTag('hltOnlineBeamSpot'),
  measTkEvt = cms.InputTag('hltSiStripClusters'),
  superClusters = cms.VInputTag('hltEgammaSuperClustersToPixelMatch'),
  matcherConfig = cms.PSet(
    useRecoVertex = cms.bool(False),
    navSchool = cms.string('SimpleNavigationSchool'),
    detLayerGeom = cms.string('hltESPGlobalDetLayerGeometry'),
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
  )
)
