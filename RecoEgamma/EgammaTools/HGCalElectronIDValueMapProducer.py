import FWCore.ParameterSet.Config as cms

def HGCalElectronIDValueMapProducer(**kwargs):
  mod = cms.EDProducer('HGCalElectronIDValueMapProducer',
    electrons = cms.InputTag('ecalDrivenGsfElectronsHGC'),
    pcaRadius = cms.double(3),
    variables = cms.vstring(
      'ecOrigEt',
      'ecOrigEnergy',
      'ecEt',
      'ecEnergy',
      'ecEnergyEE',
      'ecEnergyFH',
      'ecEnergyBH',
      'pcaEig1',
      'pcaEig2',
      'pcaEig3',
      'pcaSig1',
      'pcaSig2',
      'pcaSig3',
      'pcaAxisX',
      'pcaAxisY',
      'pcaAxisZ',
      'pcaPositionX',
      'pcaPositionY',
      'pcaPositionZ',
      'sigmaUU',
      'sigmaVV',
      'sigmaEE',
      'sigmaPP',
      'nLayers',
      'firstLayer',
      'lastLayer',
      'e4oEtot',
      'layerEfrac10',
      'layerEfrac90',
      'measuredDepth',
      'expectedDepth',
      'expectedSigma',
      'depthCompatibility',
      'caloIsoRing0',
      'caloIsoRing1',
      'caloIsoRing2',
      'caloIsoRing3',
      'caloIsoRing4'
    ),
    dEdXWeights = cms.required.vdouble,
    isoNRings = cms.uint32(5),
    isoDeltaR = cms.double(0.15),
    isoDeltaRmin = cms.double(0),
    EERecHits = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    FHRecHits = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
    BHRecHits = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
    hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod