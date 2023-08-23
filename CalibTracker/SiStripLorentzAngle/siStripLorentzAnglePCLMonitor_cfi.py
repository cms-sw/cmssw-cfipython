import FWCore.ParameterSet.Config as cms

siStripLorentzAnglePCLMonitor = cms.EDProducer('SiStripLorentzAnglePCLMonitor',
  folder = cms.string('AlCaReco/SiStripLorentzAngle'),
  saveHistoMods = cms.bool(False),
  Tracks = cms.InputTag('SiStripCalCosmics'),
  mightGet = cms.optional.untracked.vstring
)
