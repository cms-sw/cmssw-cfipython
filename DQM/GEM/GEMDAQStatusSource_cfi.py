import FWCore.ParameterSet.Config as cms

GEMDAQStatusSource = cms.EDProducer('GEMDAQStatusSource',
  digisInputLabel = cms.InputTag('muonGEMDigis'),
  VFATInputLabel = cms.InputTag('muonGEMDigis', 'vfatStatus'),
  GEBInputLabel = cms.InputTag('muonGEMDigis', 'gebStatus'),
  AMCInputLabel = cms.InputTag('muonGEMDigis', 'AMCdata'),
  AMC13InputLabel = cms.InputTag('muonGEMDigis', 'AMC13Event'),
  AMCSlots = cms.int32(13),
  logCategory = cms.untracked.string('GEMDAQStatusSource'),
  mightGet = cms.optional.untracked.vstring
)
