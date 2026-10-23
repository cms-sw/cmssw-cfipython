import FWCore.ParameterSet.Config as cms

def Type1PFMET(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
