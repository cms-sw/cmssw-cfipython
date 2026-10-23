import FWCore.ParameterSet.Config as cms

def GenTtbarCategorizer(*args, **kwargs):
  mod = cms.EDProducer('GenTtbarCategorizer',
    genJetPtMin = cms.double(20),
    genJetAbsEtaMax = cms.double(2.4),
    genJets = cms.InputTag('ak4GenJets'),
    genBHadJetIndex = cms.InputTag('matchGenBHadron', 'genBHadJetIndex'),
    genBHadFlavour = cms.InputTag('matchGenBHadron', 'genBHadFlavour'),
    genBHadFromTopWeakDecay = cms.InputTag('matchGenBHadron', 'genBHadFromTopWeakDecay'),
    genBHadPlusMothers = cms.InputTag('matchGenBHadron', 'genBHadPlusMothers'),
    genBHadPlusMothersIndices = cms.InputTag('matchGenBHadron', 'genBHadPlusMothersIndices'),
    genBHadIndex = cms.InputTag('matchGenBHadron', 'genBHadIndex'),
    genBHadLeptonHadronIndex = cms.InputTag('matchGenBHadron', 'genBHadLeptonHadronIndex'),
    genBHadLeptonViaTau = cms.InputTag('matchGenBHadron', 'genBHadLeptonViaTau'),
    genCHadJetIndex = cms.InputTag('matchGenCHadron', 'genCHadJetIndex'),
    genCHadFlavour = cms.InputTag('matchGenCHadron', 'genCHadFlavour'),
    genCHadFromTopWeakDecay = cms.InputTag('matchGenCHadron', 'genCHadFromTopWeakDecay'),
    genCHadBHadronId = cms.InputTag('matchGenCHadron', 'genCHadBHadronId'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
