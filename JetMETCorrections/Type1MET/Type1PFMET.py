import FWCore.ParameterSet.Config as cms

def Type1PFMET(**kwargs):
  mod = cms.EDProducer('Type1PFMET',
    inputUncorJetsTag = cms.InputTag('ak4PFJets'),
    jetEMfracLimit = cms.double(0.95),
    jetMufracLimit = cms.double(0.95),
    metType = cms.string('PFMET'),
    jetPTthreshold = cms.double(20),
    inputUncorMetLabel = cms.InputTag('pfMET'),
    corrector = cms.InputTag('ak4PFL2L3Corrector'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
