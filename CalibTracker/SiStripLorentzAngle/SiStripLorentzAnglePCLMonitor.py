import FWCore.ParameterSet.Config as cms

def SiStripLorentzAnglePCLMonitor(*args, **kwargs):
  mod = cms.EDProducer('SiStripLorentzAnglePCLMonitor',
    folder = cms.string('AlCaReco/SiStripLorentzAngle'),
    saveHistoMods = cms.bool(False),
    Tracks = cms.InputTag('SiStripCalCosmics'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
