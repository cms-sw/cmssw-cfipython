import FWCore.ParameterSet.Config as cms

def JetCoreClusterSplitter(*args, **kwargs):
  mod = cms.EDProducer('JetCoreClusterSplitter',
    pixelCPE = cms.string('PixelCPEGeneric'),
    verbose = cms.bool(False),
    ptMin = cms.double(200),
    deltaRmax = cms.double(0.05),
    chargeFractionMin = cms.double(2),
    pixelClusters = cms.InputTag('siPixelCluster'),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    cores = cms.InputTag('ak5CaloJets'),
    forceXError = cms.double(100),
    forceYError = cms.double(150),
    fractionalWidth = cms.double(0.4),
    chargePerUnit = cms.double(2000),
    centralMIPCharge = cms.double(26000),
    expSizeXAtLorentzAngleIncidence = cms.double(1.5),
    expSizeXDeltaPerTanAlpha = cms.double(0),
    expSizeYAtNormalIncidence = cms.double(1.3),
    tanLorentzAngle = cms.double(0),
    tanLorentzAngleBarrelLayer1 = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
