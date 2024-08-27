import FWCore.ParameterSet.Config as cms

def PUFilter(**kwargs):
  mod = cms.EDProducer('PUFilter',
    Jets = cms.InputTag('hltAK4PFJetsCorrected'),
    JetPUID = cms.InputTag('MVAJetPuIdProducer', 'CATEv0Id'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
