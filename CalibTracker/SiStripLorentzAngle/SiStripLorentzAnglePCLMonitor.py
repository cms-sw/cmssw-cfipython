import FWCore.ParameterSet.Config as cms

def SiStripLorentzAnglePCLMonitor(**kwargs):
  mod = cms.EDProducer('SiStripLorentzAnglePCLMonitor',
    folder = cms.string('AlCaReco/SiStripLorentzAngle'),
    saveHistoMods = cms.bool(False),
    Tracks = cms.InputTag('SiStripCalCosmics'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
