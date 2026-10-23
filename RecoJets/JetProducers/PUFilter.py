import FWCore.ParameterSet.Config as cms

def PUFilter(*args, **kwargs):
  mod = cms.EDProducer('PUFilter',
    Jets = cms.InputTag('hltAK4PFJetsCorrected'),
    JetPUID = cms.InputTag('MVAJetPuIdProducer', 'CATEv0Id'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
