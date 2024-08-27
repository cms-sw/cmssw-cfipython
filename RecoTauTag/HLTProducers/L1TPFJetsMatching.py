import FWCore.ParameterSet.Config as cms

def L1TPFJetsMatching(**kwargs):
  mod = cms.EDProducer('L1TPFJetsMatching',
    L1JetTrigger = cms.InputTag('hltL1DiJetVBF'),
    JetSrc = cms.InputTag('hltAK4PFJetsTightIDCorrected'),
    matchingMode = cms.string('VBF'),
    pt1Min = cms.double(110),
    pt2Min = cms.double(35),
    pt3Min = cms.double(110),
    mjjMin = cms.double(650),
    matchingR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
