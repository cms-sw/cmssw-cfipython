import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationByIPCut(**kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationByIPCut',
    tausTIP = cms.InputTag('hltTauIPCollection'),
    cut = cms.string('abs(dxy) > -999.'),
    PFTauProducer = cms.InputTag('fixme'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('AND'),
      leadTrack = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      ),
      decayMode = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
