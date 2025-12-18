import FWCore.ParameterSet.Config as cms

def MVAJetPuIdProducer(*args, **kwargs):
  mod = cms.EDProducer('MVAJetPuIdProducer',
    runMvas = cms.bool(True),
    inputIsCorrected = cms.bool(True),
    vertexes = cms.InputTag('hltPixelVertices'),
    produceJetIds = cms.bool(True),
    jec = cms.string('AK4PF'),
    residualsFromTxt = cms.bool(False),
    applyJec = cms.bool(False),
    jetids = cms.InputTag(''),
    rho = cms.InputTag('hltFixedGridRhoFastjetAll'),
    jets = cms.InputTag('hltAK4PFJetsCorrected'),
    algos = cms.VPSet(
      template = cms.PSetTemplate(
        tmvaVariables = cms.vstring(
          'rho',
          'nParticles',
          'nCharged',
          'majW',
          'minW',
          'frac01',
          'frac02',
          'frac03',
          'frac04',
          'ptD',
          'beta',
          'betaStar',
          'dR2Mean',
          'pull',
          'jetR',
          'jetRchg'
        ),
        tmvaMethod = cms.string('JetID'),
        cutBased = cms.bool(False),
        tmvaWeights = cms.string('RecoJets/JetProducers/data/MVAJetPuID.weights.xml.gz'),
        tmvaSpectators = cms.vstring(
          'jetEta',
          'jetPt'
        ),
        label = cms.string('CATEv0'),
        version = cms.int32(-1),
        JetIdParams = cms.PSet(
          Pt2030_Tight = cms.vdouble(
            0.73,
            0.05,
            -0.26,
            -0.42
          ),
          Pt2030_Loose = cms.vdouble(
            -0.63,
            -0.6,
            -0.55,
            -0.45
          ),
          Pt3050_Medium = cms.vdouble(
            0.1,
            -0.36,
            -0.54,
            -0.54
          ),
          Pt1020_Tight = cms.vdouble(
            -0.83,
            -0.81,
            -0.74,
            -0.81
          ),
          Pt2030_Medium = cms.vdouble(
            0.1,
            -0.36,
            -0.54,
            -0.54
          ),
          Pt010_Tight = cms.vdouble(
            -0.83,
            -0.81,
            -0.74,
            -0.81
          ),
          Pt1020_Loose = cms.vdouble(
            -0.95,
            -0.96,
            -0.94,
            -0.95
          ),
          Pt010_Medium = cms.vdouble(
            -0.83,
            -0.92,
            -0.9,
            -0.92
          ),
          Pt1020_Medium = cms.vdouble(
            -0.83,
            -0.92,
            -0.9,
            -0.92
          ),
          Pt010_Loose = cms.vdouble(
            -0.95,
            -0.96,
            -0.94,
            -0.95
          ),
          Pt3050_Loose = cms.vdouble(
            -0.63,
            -0.6,
            -0.55,
            -0.45
          ),
          Pt3050_Tight = cms.vdouble(
            0.73,
            0.05,
            -0.26,
            -0.42
          )
        ),
        impactParTkThreshold = cms.double(1)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
